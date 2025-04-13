# Easter Date Calculator 🕊

This Python script calculates the date of **Catholic** and **Orthodox Easter** in the Gregorian calendar for any year between **1500 and 3000**.

It uses:
- The **Meeus/Jones/Butcher algorithm** for calculating **Catholic Easter**
- A **Julian calendar-based algorithm** for **Orthodox Easter**, with conversion to the **Gregorian calendar**

🗓 Orthodox Easter is shown **in both the Julian and Gregorian calendars**.

---

## How to use

Run the script in a Python environment:

```bash
python easter.py
```

You will be prompted to enter a year (e.g., `2025`) and receive both Easter dates.

---

## Example output

```
Date of Catholic and Orthodox Easter (Gregorian calendar)
Enter a year between 1500 and 3000: 2025

Catholic Easter: 4.20
Orthodox Easter: 4.20 (4.7)
```

Here:
- `4.20` = Orthodox Easter (Gregorian calendar)
- `(4.7)` = Orthodox Easter (Julian calendar)

---

## 🚀 Future Plans

- [ ] Add function to find all years when **Catholic and Orthodox Easter coincide**
- [ ] Add feature to check if a given **birthday** ever coincides with Easter


## License

MIT License. Feel free to use or modify.
