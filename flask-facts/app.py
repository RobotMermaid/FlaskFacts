from flask import Flask, render_template
import os
import random

app = Flask(__name__)

facts = [
    {
        "content": "Ondine is an excellent person to have on your team.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "She works very well with others and quite naturally builds relationships.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "Ondine has a positive influence on the spirit and morale of those that work with her.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "Ondine is especially helpful and patient when teaching and explaining the current state of her features and bugs. This makes it very easy to learn from, and plan around her work.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "She’s responsible, hardworking, committed. She thinks carefully about the problem and provides very good recommendations for intuitive interface.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "Ondine takes her job seriously and approaches her tasks with discipline and diligence.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "She understands her role and responsibilities clearly and is always willing to make an effort to contribute to the company’s need for better API and deliverables. For an example, last time she was little worried that her tickets would not be completed before her vacations - she put extra hours and tried to reach others so that she could complete it (which she could had done after returning).",
        "source": "Praveen Kumar (co-worker)"
    }, {
        "content": "Developers like her are assets - who’re committed to get things done asap.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "She is an excellent judge of character and provides counsel in hiring situations.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "She is responsible for almost all of the API development that has gone on at Riffyn over this past year and exhibits a sense of accountability toward issues with the endpoints.",
        "source":  "Annual Performance Review 2020"
    }, {
        "content": "Ondine has great intuition with regards to people and I value her input when making decisions about personnel and team dynamics.",
        "source":  "Larry Peck - VP of engineering"
    }, {
        "content": "Ondine - thanks for nurturing our API to adulthood and breathing life into our culture and values.",
        "source": "Tim Gardner - CEO of Riffyn Inc"
    }, {
        "content": "She embraces learning, accepts new challenges, and shows terrific discipline, communication and consistency.",
        "source": "Annual Performance Review 2019"
    }, {
        "content": "Impressive execution of the api key and access token stories. with little interaction needed. We just explained the need for the enhancementand high level implementation. She got the problem and ran with it.",
        "source": "Annual Performance Review 2019"
    }, {
        "content": "We can rely on Ondine, and that is immensely valuable to the effectiveness of our organization.",
        "source": "Annual Performance Review 2019"
    }, {
        "content": "In her own quiet way she adds to and enhances the honest and sincere culture of Riffyn.",
        "source": "Annual Performance Review 2019"
    },{
        "content": "Thanks a million Ondine!  You are a star!  ... Er I mean a rocket mermaid.  Or is it mermaid rocket?  Or Mercket?",
        "source": "Tim Gardner - CEO of Riffy Inc."
    }, {
        "content": "“Excellent. This is a very useful tool.",
        "source": "Tim Gardner - CEO of Riffyn Inc. (in regards to the Clone Process Endpoint)"
    }
]


@app.route("/")
def index():
    myFacts = random.choice(facts)
    return render_template("index.html", fact = myFacts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
