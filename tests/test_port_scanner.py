import socket
import unittest


from vulnscan.port_scanner import(
   validate_target,
   scan_ports
)



class TestPortScanner(unittest.TestCase):
   def test_valid_ip(self):
      self.assertEqual(
         validate_target("127.0.0.1"),
         "127.0.0.1"
      )

   def test_invalid_ip(self):
      with self.assertRaises(ValueError):
         validate_target("999.999.999.999")

   def test_open_port(self):

      server =socket.socket(
         socket.AF_INET,
         socket.SOCK_STREAM
      )

      server.bind(("127.0.0.1",0))
      server.listen(1)

      port = server.getsockname()[1]

      try:
         results = scan_ports(
            "127.0.0.1",
            [port],
            timeout = 1
         )

         self.assertEqual(len(results),1)
         self.assertEqual(results[0].state, "open")

      finally:
         server.close()

if __name__ == "__main__":
   unittest.main()