FROM ktaskn/notebook

ENV WORKDIR /workspace

COPY requirements.txt $WORKDIR/requirements.txt

WORKDIR $WORKDIR
RUN pip install -U pip && pip install -r requirements.txt