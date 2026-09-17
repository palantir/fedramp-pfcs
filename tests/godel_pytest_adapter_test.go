package tests

import (
	"os"
	"os/exec"
	"testing"
)

// TestPytestAdapter forwards pytest output and failures to Godel's Go test runner.
func TestPytestAdapter(t *testing.T) {
	cmd := exec.Command("sh", "scripts/python.sh", "-u", "-m", "pytest", "-q")
	cmd.Dir = ".."
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		t.Fatalf("pytest failed: %v", err)
	}
}
