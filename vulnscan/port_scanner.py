import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass

@dataclass
class PortResult:
   port:int
   state:str
   service:str

def validate_target(target:str)-> str:
   # to check if the target ip is either in v4 or v6 format.
   try:
      return str(ipaddress.ip_address(target))
   except ValueError:
      raise ValueError("INVALID IP ADDRESS")

def identify_service(port: int)->str:
   #Identify common TCP service names

   try:
      return socket.getservbyport(port,"tcp")
   except OSError:
      return "UNKNOWN"

def scan_port (target: str, port:int, timeout:float)-> PortResult:
   try:
      with socket.create_connection((target,port), timeout=timeout):
         return PortResult(
            port=port,
            state="open",
            service=identify_service(port)
         )
   except socket.timeout:
      return PortResult(port,"FILTERED","UNKNOWN")
   except ConnectionRefusedError:
      return PortResult(port, "CLOSED", "UNKNOWN")
   except OSError:
      return PortResult(port, "UNKNOWN", "UNKNOWN")

def scan_ports(target: str, ports:list, timeout:float=1.0, max_workers: int = 100) -> list:
   #To scan multiple ports

   target = validate_target(target)

   if not 0 <timeout <=30:
      raise ValueError("Timeout must be greater than 0 and at most 30 seconds.")

   if not 1 <= max_workers <= 500:
      raise ValueError("Workers must be between 1 and 500")

   if not ports:
      raise ValueError("Atleast 1 port must be provided")

   if any (
      isinstance(port,bool)
      or not isinstance(port, int)
      or not 1 <= port <= 65535
      for port in ports
   ):
      raise ValueError("Ports must be integers between 1 and 65535.")
   results = []

   with ThreadPoolExecutor(max_workers=max_workers) as executor:
      futures = {
         executor.submit(scan_port, target, port, timeout): port
         for port in set(ports)
      }

      for future in as_completed(futures):
         result = future.result()
         results.append(result)

   return sorted(results, key=lambda result: result.port)