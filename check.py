import os

def check_reboot():
	"""Returns True if the computer has apending reboot."""
	returen os.path.exist("/run/reboot-required")

def main():
	pass

main()
