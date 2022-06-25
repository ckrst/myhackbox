#!/bin/bash
openssl genrsa -out keypair.pem 2048
openssl rsa -in keypair.pem -pubout -out public.crt
openssl pkcs8 -topk8 -inform PEM -outform PEM -nocrypt -in keypair.pem -out pkcs8.pem