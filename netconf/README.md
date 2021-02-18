# netconf notes


## Example

```python
from ncclient import manager

# From Linux Node
# ssh -oHostKeyAlgorithms=+ssh-dss developer@10.10.20.48 -p 830 -s netconf

# Once connected to say hello back 
"""
 <?xml version="1.0" encoding="UTF-8"?>
 <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <capabilities>
   <capability>urn:ietf:params:netconf:base:1.0</capability>
 </capabilities>
   </hello>]]>]]>
"""

# To Close the session
"""
 <?xml version="1.0" encoding="UTF-8"?>
 <rpc message-id="1239123" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <close-session />
 </rpc>
 ]]>]]>
 """

# Understanding NETCONF Operations
"""
<get>	            Retrieve running configuration and device state information.
<get-config>	    Retrieve all or part of specified configuration datastore.
<edit-config>	    Load all or part of a configuration to the specified configuration datastore.
<copy-config>	    Replace an entire configuration datastore with another.
<delete-config>	    Delete a configuration datastore.
<commit>	        Copy candidate datastore to running datastore.
<lock> / <unlock>	Lock or unlock the entire configuration datastore computer.
<close-session>	    Close the NETCONF session gracefully.
<kill-session>	    Force the NETCONF session to end.
"""

interface = {
    "interfaces": [
        {
            "interface": "Ethernet1/1",
            "vlan": "1",
            "type": "eth",
            "portmode": "fabric",
            "state": "down",
            "state_rsn_desc": "SFP not inserted",
            "speed": "10G",
            "ratemode": "D"
        }    
    ]
}

manager = manager.connect(
  host=env_lab.
)
```