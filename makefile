calc:
        python3 ./sources/add2vals.py ${num1} ${num2}

install:
        python3 -m pip install -r requirements.txt

app:
        sudo docker build -f Dockerfile-PyApp . --tag simple-pyhton:1.0.0

container:
        sudo docker run --rm -d --name simple-pyhton -p 3000:3000 simple-pyhton:1.0.0

stop:
        sudo docker stop simple-pyhton