#!/usr/bin/python3

# *****************************************************************************
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# ******************************************************************************

import argparse
import json
import sys
from datalab.actions_lib import *
from datalab.meta_lib import *

parser = argparse.ArgumentParser()
parser.add_argument('--firewall', type=str)
args = parser.parse_args()

if __name__ == "__main__":
    firewall = json.loads(args.firewall)
    if firewall:
        for firewall_rule in firewall['ingress']:
            if GCPMeta().get_firewall(firewall_rule['name']):
                print("REQUESTED INGRESS FIREWALL {} ALREADY EXISTS".format(firewall_rule['name']))
            else:
                print("Creating Ingress Firewall {}".format(firewall_rule['name']))
                GCPActions().create_firewall(firewall_rule)
        for firewall_rule in firewall['egress']:
            if GCPMeta().get_firewall(firewall_rule['name']):
                print("REQUESTED EGRESS FIREWALL {} ALREADY EXISTS".format(firewall_rule['name']))
            else:
                print("Creating Egress Firewall {}".format(firewall_rule['name']))
                GCPActions().create_firewall(firewall_rule)
    else:
        parser.print_help()
        sys.exit(2)
