# Galley

A small tool for managing manifests of projects distributed as monolithic YAML files.

Many kube-native projects these days are distributed as single YAML files. This is fine for trying things out in dev but for managing production deployments is unacceptable. `Dekompose` tries to implement a simple workflow for configuring and upgrading discrete manifests for projects like this. It was developed primarily to work well with kustomize but can be of value for those deploying vanilla manifests as well.

## TODO
** Make sure none have the same filename
** Change file names if theres collision
** Make the names of files kebab-case.
** Display mappings (oldpath -> newpath) and net new files before writing
** Display diffs before writing as well, or dont - let git do that
## DONE
* create an example using two versions of argocd and see what happens
* write out the individual yaml files for all new resources
* a bunch of crap
