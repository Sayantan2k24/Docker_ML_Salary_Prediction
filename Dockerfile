FROM centos

RUN yum install python3 -y

RUN pip3 install pandas

RUN pip3 install scikit-learn

COPY sal_demo.py sal_code.py

COPY SalaryData.csv SalaryData.csv

ENTRYPOINT [ "python3", "sal_code.py" ]

CMD ["1.4"]


