all:
	docker build -t thotypous/alpine-net-lab -f Dockerfile.alpine
	docker build -t thotypous/kali-net-lab -f Dockerfile.kali
	docker build -t thotypous/vsftpd-net-lab -f Dockerfile.vsftpd
	docker push thotypous/alpine-net-lab
	docker push thotypous/kali-net-lab
	docker push thotypous/vsftpd-net-lab
