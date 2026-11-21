import argparse
import time

from port_scanner import scan_ports


def main():
   parser = argparse.ArgumentParser(
      description="VulnScan - TCP Post Scanner"
   )

   parser.add_argument(
      "--target",
      required=True,
      help="Target IPv4 or IPv6 address"
   )

   parser.add_argument(
      "--start-port",
      type=int,
      default=1,
      help="Starting TCP port (default: 1)"
   )

   parser.add_argument(
      "--end-port",
      type=int,
      default=1024,
      help="Ending TCP port (default: 1024)"
   )

   parser.add_argument(
      "--timeout",
      type=float,
      default=1.0,
      help="Connection timeout in seconds"
   )

   parser.add_argument(
      "--workers",
      type=int,
      default=100,
      help="Maximum concurrent workers(default:100)"
   )

   args = parser.parse_args()

   if not (
      1<=args.start_port <= args.end_port<= 65535
   ):
      parser.error("Invalid port range")

   print("="*55)
   print("             VulnScan v0.1")
   print("="*55)


   print(f"Target        : {args.target}")
   print(f"Port Range    : {args.start_port}---{args.end_port}")
   print(f"Timeout       : {args.timeout}s")
   print(f"Workers       : {args.workers}")

   print("\n[*] Starting TCP scan...\n")

   start_time = time.perf_counter()

   try:
      results = scan_ports(
         target=args.target,
         ports=range(args.start_port, args.end_port + 1),
         timeout=args.timeout,
         max_workers=args.workers
      )
   except ValueError as error:
      parser.error(str(error))


   open_ports= [
      result for result in results
      if result.state == "open"
   ]

   elapsed = time.perf_counter() - start_time

   print("\n" + "-" * 55)
   print("SCAN RESULTS")
   print("-" * 55)

   if open_ports:
      for result in open_ports:
         print(
            f"[OPEN] {result.port}/tcp"
            f"- {result.service}"
         )
   else:
      print("No Open TCP ports identified.")
   
   
   print("\n" + "-" * 55)
   print(f"Ports scanned : {len(results)}")
   print(f"Open ports    : {len(open_ports)}")
   print(f"Scan duration : {elapsed:.2f} seconds")
   print("\n" + "-" * 55)


if __name__ == "__main__":
   main()