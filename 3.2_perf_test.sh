echo "Installing perf and stress"
apt update && apt install -y linux-tools-common linux-tools-generic linux-tools-$(uname -r) stress

echo "User process limit:"
ulimit -a | grep "max user processes"

echo "Running stress for 10 seconds on 4 CPU cores..."
stress --cpu 4 --timeout 10
