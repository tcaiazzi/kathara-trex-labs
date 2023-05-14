# kathara-trex-labs
This repository contains a collection of Kathará network scenarios for testing the 
[TRex](https://trex-tgn.cisco.com/) traffic generator.

If you need to test/learn TRex this is the simplest way!

## Resources
In the following you can find some links to useful resources:
- [Kathará Official Website](https://www.kathara.org/)
- [Kathará Repository](https://github.com/KatharaFramework/Kathara)
- [TRex Official Website](https://trex-tgn.cisco.com/)
- [TRex Repository](https://github.com/cisco-system-traffic-generator/trex-core)

## Pre-Requisites (5 minutes instructions)

1. To run the network scenarios you need to install the Kathará network emulator (support for all the OSes). 
You can follow the official [installation guide](https://github.com/KatharaFramework/Kathara/wiki/Installation-Guides).
2. You need to build the Docker TRex image.
```shell
docker build -t kathara/trex dockerfile/
```

## Advanced Stateful Network Scenarios
The `astf` directory contains network scenarios that use the [TRex ASTF API](https://trex-tgn.cisco.com/trex/doc/cp_astf_docs/api/index.html):
- [base_scenario](astf/base_scenario): a simple network scenario composed by three devices. It deploys a TRex server on a node and 
a TRex client on another, using the interactive API to generate http traffic between them. 

- [simple_fat_tree](astf/simple_fat_tree): a network scenario to test the data-plane of a simple fat-tree data center composed of two pods and ten switches. The fat-tree uses a BGP control-plane implemented using FRRouting to exchange routes among nodes.

## Kathará Labs
If you liked Kathará, you can find more resources that span several network scenarios and technologies on the official [Kathará-Labs](https://github.com/KatharaFramework/Kathara-Labs)
repository.
