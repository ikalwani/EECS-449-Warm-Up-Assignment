walker interact {
    can return_message with `root entry {
        report {
            "response": "Hello, world!"
        };
    }
}

walker interact_with_body {
    has name: str;

    can return_message with `root entry {
        report {
            "response": "Hello, " + self.name + "!"
        };
    }
}

walker add_two_str {
    has s1: str;
    has s2: str;
    can return_message with `root entry {
        report {
            "response": self.s1 + " " + self.s2
        };
    }
}

walker simple_interest {
    has principal: float;
    has rate: float; 
    has time: float;

    can return_message with entry {
        report {
            "response": "Simple Interest: " + str((self.principal * self.rate * self.time) / 100) + " USD"
        };
    }
}