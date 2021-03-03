# IOS-XR Notes

## Configuring SSH

Verify that you have k9sec installed

```bash
RP/0/0/CPU0:ios#show install active | include k9
```

Next generate RSA/DSA key pair

**RSA** - SSHv1

**DSA** - SSHv2

```bash
RP/0/0/CPU0:ios#crypto key generate dsa

Wed Mar  3 16:59:27.566 UTC

The name for the keys will be: the_default
  Choose the size of your DSA key modulus. Modulus size can be 512, 768, or 1024 bits. Choosing a key modulus

How many bits in the modulus [1024]: 2048

Generating DSA keys ...
Done w/ crypto generate keypair
[OK]
```

Now enable the ssh server on the XR device

NOTE: You have the ability to enable ssh per vrf

```bash
RP/0/0/CPU0:ios#config t
Wed Mar  3 17:00:26.702 UTC
RP/0/0/CPU0:ios(config)#ssh server v2
```
