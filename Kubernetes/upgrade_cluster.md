# Steps to Upgrade Kubernetes running on Debian distribution

## Upgrade Controller Node
- List all the nodes and controllers and drain the controller
  `kubectl get node`
  `kubectl drian [controller-name]`
- Upgrade the local repository and upgrade kubeadm
  `sudo apt update`
  `sudo apt install -y kubeadm=[version]`
