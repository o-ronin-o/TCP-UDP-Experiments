PYTHON=python3

# --------------------
# TCP
# --------------------

tcp-server:
	$(PYTHON) tcp_server.py

tcp-client:
	$(PYTHON) tcp_client.py

# --------------------
# UDP
# --------------------

udp-server:
	$(PYTHON) udp_server.py

udp-client:
	$(PYTHON) udp_client.py

# --------------------
# Run both (separate terminals recommended)
# --------------------

run-tcp:
	@echo "Start server first in another terminal:"
	@echo "make tcp-server"
	@echo "Then run:"
	@echo "make tcp-client"

run-udp:
	@echo "Start server first in another terminal:"
	@echo "make udp-server"
	@echo "Then run:"
	@echo "make udp-client"

# --------------------
# Clean
# --------------------

clean:
	rm -rf __pycache__ *.pyc
