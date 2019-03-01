
def log_fw(ip, rules):
    """
    Take in string, which will be all iptables output, split it into one rule per line, log in form:
    IP      FIREWALL        <RULE>
    so each line of log file has one rule
    @param ip: The source IP address, will be used as identifer
    @param rules: the output of all the iptables commands (including newlines)
    @return: None    
    """
    rlist = rules.split("\n")
    print(rlist)
    with open('/tmp/mm/logs/input.log', 'w') as f:
        f.write("writing...")
        for rule in rlist:
            rule = rule.rstrip()
            f.write(rule + "\n")
    return


def log_hosts(ip, hosts):
    """
    Take in string, which will be the /etc/hosts file, split it into one host per line, log in form:
    IP      HOSTS        <host_ip>       <hostname>
    so each line of log file has "host" entry
    @param ip: The source IP address, will be used as identifer
    @param hosts: the output of "cat /etc/hosts" (including newlines)
    @return: None    
    """
    for host in hosts:
        print(host)
    return


def log_routes(ip, routes):
    """
    Take in string, which will be all ip routes output, split it into one route per line, log in form:
    IP      ROUTE        <Route Data>
    so each line of log file has one route
    @param ip: The source IP address, will be used as identifer
    @param routes: the output of the "ip route" (including newlines)
    @return: None    
    """
    for route in routes:
        print(route)
    return


def log_arp(ip, arp):
    """
    Take in string, which will be arp table, split it into one entry per line, log in form:
    IP      ARP        <entry>
    so each line of log file has one arp entry
    @param ip: The source IP address, will be used as identifer
    @param arp: output of "arp -a" (including newlines)
    @return: None    
    """
    for entry in arp:
        print(entry)
    return
