$TTL 86400
@   IN  SOA    com. root.com. (
        2011071001  ;Serial
        10        ;Refresh
        5        ;Retry
        10      ;Expire
        20       ;Minimum TTL
)
@	IN  NS		t1a.com.
@	IN  A		192.168.219.20
web.t1a	IN  NS		t1a.com.
api.apidns.t1a	IN	NS	apidns.t1a.com.
apidns.t1a	IN  NS		t1a.com.
api.t1a		IN	CNAME	api.apidns.t1a.com.
t1a	IN  A		192.168.219.20
