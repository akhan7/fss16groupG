### Generic Experiments

> Purpose of this exercise is to build a generic model that acts as base for any
model like Schaffer, Osyczka2 or Kursawe

To calculate the score of a model
```python
    def evaluate(self, point):
        return self.normalize(self.__eval(point))
```

To check if the point abides by the constraints of the model
```python
    def is_valid(self, point):
        if self.constraints != None:
            return self.constraints(point)
        return True
```

To random generate a point that satifies the constraints of the model
```python
    def generate_one(self):
        while True:
            point = []
            for decision in self.decisions:
                point.append(random.randint(decision.low, decision.high))
            valid = self.is_valid(point)
            if valid:
                return point
```

To calculate the min-max of a model over 1000 tries (the value retured by this
function is used for normalization of values)
```python
    def get_min_max(self, retries=1000):
        scores = []
        for i in xrange(retries):
            scores.append(self.__eval(self.generate_one()))

        return min(scores), max(scores)
```

To normalize the score of a model (at a point) between 0 and 1
```python
    def normalize(self, score):
        return (score - self.min) / float(self.max - self.min)
```

To denormalize a value between 0 and 1 to the actual score
```python
    def denormalize(self, normal_val):
        """Converts normalized value to actual value"""
        return normal_val * (self.max - self.min) + self.min
```


####generic.py
```python
for model in [Schaffer, Osyczka2, Kursawe]:
    for optimizer in [SA, MWS]:
           optimizer(model()).run()
```

### Output

Schaffer evaluated by SA
[]()