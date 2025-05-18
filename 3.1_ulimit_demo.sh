echo "Soft limit (nofile):"
ulimit -n

echo "All soft limits:"
ulimit -aS | grep "open files"

echo "All hard limits:"
ulimit -aH | grep "open files"

echo "Setting soft limit to 3000"
ulimit -n 3000
ulimit -aS | grep "open files"

echo "Try setting soft limit to 3001 (should fail)"
ulimit -n 3001

echo "Setting soft limit to 2000"
ulimit -n 2000
ulimit -n
ulimit -aS | grep "open files"
ulimit -aH | grep "open files"

echo "Try setting soft limit back to 3000"
ulimit -n 3000
