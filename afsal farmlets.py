{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5f18748d-282d-4156-8a21-18af430ebf9b",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import scipy.stats as stats\n",
    "import statsmodels.api as sm\n",
    "from statsmodels.formula.api import ols"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5b880457-078b-494e-9f14-bcc161ab10d1",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "file_path = 'D:\\\\data science exam\\\\afsal.csv'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6e16568d-988c-4e63-a368-d8910adae400",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "data = pd.read_csv('D:\\\\data science exam\\\\afsal.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "02852d8d-0fa3-4069-af9f-efba308fe880",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "independent_var = 'Farmlet'  \n",
    "dependent_vars = data.columns.drop(['Date', 'Time', 'Reporter', 'Farmlet'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "23dd4780-b516-4636-a764-0f508cdfd347",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "anova_results = {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7092a99c-3058-4cca-80f3-c4a8bd9dd6f6",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "independent_var = 'Farmlet'\n",
    "dependent_vars = data.columns.drop(['Date', 'Time', 'Reporter', 'Farmlet'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "813862f2-aa47-401f-b843-d45268935034",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def load_data(filepath):\n",
    "    \"\"\"D:\\\\data science exam\\\\afsal.csv\"\"\"\n",
    "    return pd.read_csv(filepath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "55294784-d2d2-4fa0-9025-eb40dbe0af78",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def perform_anova(data):\n",
    "    emotional_states = ['Active', 'Relaxed', 'Fearful', 'Agitated', 'Calm', 'Content', 'Indifferent', 'Frustrated']\n",
    "    anova_results = {}\n",
    "    for state in emotional_states:\n",
    "        groups = data.groupby('Farmlet')[state].apply(list)\n",
    "        anova_results[state] = f_oneway(*groups)\n",
    "    return anova_results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "928c1755-86aa-4a66-89d7-301ee674088f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def main():\n",
    "    data = load_data('afsal.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "86159880-eb69-4c0a-abac-5fa2b97f3454",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def perform_anova(data):\n",
    "    emotional_states = ['Active', 'Relaxed', 'Fearful', 'Agitated', 'Calm', 'Content', 'Indifferent', 'Frustrated']\n",
    "    anova_results = {}\n",
    "    for state in emotional_states:\n",
    "        groups = data.groupby('Farmlet')[state].apply(list)\n",
    "        anova_results[state] = f_oneway(*groups)\n",
    "    return anova_results\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "4c4f8bfe-bee6-4e87-89be-c056476c8903",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def main():\n",
    "    data = load_data('afsal.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "0e294162-90e9-4f2d-80b4-e09d6e66f24f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from scipy.stats import f_oneway\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "bd16ef09-959c-40f0-abe7-1cbdc49fc02d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "groups = data.groupby('Farmlet')[state].apply(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "ab45ffff-a1e0-44dc-ab26-1f8be764f27d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "anova_result = f_oneway(*groups)\n",
    "anova_results[state] = {'p-value': anova_result.pvalue, 'F-statistic': anova_result.statistic}\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "a17a8605-1550-4cd5-a955-dab2df3c71ce",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "anova_results = perform_anova(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "ec879128-94d0-4419-8fb8-6f3fe8b75a19",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "State: Active, p-value: 0.6529, F-statistic: 0.4305\n",
      "State: Relaxed, p-value: 0.7698, F-statistic: 0.2631\n",
      "State: Fearful, p-value: 0.6558, F-statistic: 0.4259\n",
      "State: Agitated, p-value: 0.7378, F-statistic: 0.3062\n",
      "State: Calm, p-value: 0.5108, F-statistic: 0.6819\n",
      "State: Content, p-value: 0.3047, F-statistic: 1.2205\n",
      "State: Indifferent, p-value: 0.8280, F-statistic: 0.1895\n",
      "State: Frustrated, p-value: 0.4668, F-statistic: 0.7750\n"
     ]
    }
   ],
   "source": [
    "for state, result in anova_results.items():\n",
    "    print(f\"State: {state}, p-value: {result.pvalue:.4f}, F-statistic: {result.statistic:.4f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "a9b60f53-d14f-4918-adfc-701bcde647f5",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def plot_anova_results(anova_results):\n",
    "    \"\"\"Plots the ANOVA results.\"\"\"\n",
    "    states = list(anova_results.keys())\n",
    "    p_values = [result['p-value'] for result in anova_results.values()]\n",
    "    f_statistics = [result['F-statistic'] for result in anova_results.values()]\n",
    "\n",
    "    fig, ax1 = plt.subplots()\n",
    "\n",
    "    color = 'tab:red'\n",
    "    ax1.set_xlabel('Emotional State')\n",
    "    ax1.set_ylabel('p-value', color=color)\n",
    "    ax1.bar(states, p_values, color=color)\n",
    "    ax1.tick_params(axis='y', labelcolor=color)\n",
    "\n",
    "    ax2 = ax1.twinx()  \n",
    "    color = 'tab:blue'\n",
    "    ax2.set_ylabel('F-statistic', color=color)  \n",
    "    ax2.plot(states, f_statistics, color=color)\n",
    "    ax2.tick_params(axis='y', labelcolor=color)\n",
    "\n",
    "    fig.tight_layout()  \n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "176cb532-30b6-42b8-b2e9-ff57467baefb",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def main():\n",
    "    # Load the dataset (update the file path as needed)\n",
    "    data = load_data('D:\\\\data science exam\\\\afsal.csv')\n",
    "\n",
    "    # Perform ANOVA on the dataset\n",
    "    anova_results = perform_anova(data)\n",
    "\n",
    "    # Plot the ANOVA results\n",
    "    plot_anova_results(anova_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e55e5762-1d06-4181-b8b6-aee8c26238bf",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def plot_anova_results(anova_results):\n",
    "    \"\"\"Plots the ANOVA results.\"\"\"\n",
    "    states = list(anova_results.keys())\n",
    "    p_values = [result.pvalue for result in anova_results.values()]  # Correctly accessing p-value\n",
    "    f_statistics = [result.statistic for result in anova_results.values()]  # Correctly accessing F-statistic\n",
    "\n",
    "    fig, ax1 = plt.subplots()\n",
    "\n",
    "    color = 'tab:red'\n",
    "    ax1.set_xlabel('Emotional State')\n",
    "    ax1.set_ylabel('p-value', color=color)\n",
    "    ax1.bar(states, p_values, color=color)\n",
    "    ax1.tick_params(axis='y', labelcolor=color)\n",
    "\n",
    "    ax2 = ax1.twinx()  \n",
    "    color = 'tab:blue'\n",
    "    ax2.set_ylabel('F-statistic', color=color)  \n",
    "    ax2.plot(states, f_statistics, color=color)\n",
    "    ax2.tick_params(axis='y', labelcolor=color)\n",
    "\n",
    "    fig.tight_layout()  \n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "b76af177-6e4d-4240-a7d4-31cc10cad6f4",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def main():\n",
    "    data = load_data('D:\\\\data science exam\\\\afsal.csv')\n",
    "    anova_results = perform_anova(data)\n",
    "    plot_anova_results(anova_results)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "e6dc4f43-d0da-4a7b-a412-ec335ad4dec7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "df50d450-fea9-478e-843d-8289380da11a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "def main():\n",
    "    data = load_data('D:\\\\data science exam\\\\afsal.csv')\n",
    "    anova_results = perform_anova(data)\n",
    "    plot_anova_results(anova_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "b7778da5-3ba1-4fc5-a13a-9acfd751893e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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5x6h1Wqtyp2YZ05HRUUJlUolgoODxbXXXiv+/vtvy3EfffSRCAsLE66urmLGjBl2KXciRP2s8vvvv19ERkYKtVotQkNDxTXXXGMZkN7a32tTE0uael81NRGhPe+jpeVOzvf6669byl8IUT9xa+TIkcLV1dWq3MmlPn9aMhnoxx9/FJ6enkImk1nKnVzqmBMnToixY8cKtVotevbsKTZt2mSXyRO23lNrjzO/Ly68r759+wpvb2+hVCqtfv6JiYmWn//AgQMt5V3Mv+Pnn39exMXFCVdXV+Hn5ydmzpwp0tPTLcd/8MEHIjw8XMjl8kblTi60du1aERUVJTQajRg1apT48ccfG/0sn3vuOREcHCxkMplVuZOO+KzuymRCsEObiFrnhRdewLvvvovTp09LHQoREZ2HY+yI6JLefvttDBs2DFqtFjt27MArr7ximShDRESOg4kdEV3SyZMn8a9//QvFxcWIiIjAY489hiVLlkgdFhERXYBdsUREREROgrNiiYiIiJwEEzsiIiIiJ8HEjoiIiMhJMLEjIiIichJM7IiIiIicBBM7InJYy5cvx8CBAzv8uhMnTsTDDz/c4dclImorJnZEZLFw4ULIZLJGj2nTprX7tWUyWaPFvx9//HFs2bKl3a/dWkajEQkJCejduzdcXV3h5+eHkSNHYvXq1ZZ9bE0OFy5ciFmzZtkvWCLqUligmIisTJs2zSpBAQCNRiNJLB4eHvDw8JDk2hezfPlyvP/++/jPf/6DoUOHory8HPv372/R4vRERO2JLXZEZEWj0SA4ONjq4evra3ldJpPhvffew9VXXw03NzfExcVh165dSE1NxcSJE+Hu7o5Ro0YhLS3N6rzvvPMOYmJioFar0atXL3z22WeW16KiogAA1157LWQymeX5hV2xJpMJzz33HMLCwqDRaDBw4EBs2rTJ8npmZiZkMhm+/fZbTJo0CW5ubhgwYAB27dpl2aeoqAjz589HWFgY3Nzc0K9fP3z55Zet+hmtX78e9913H+bOnYvo6GgMGDAAd9xxBx599FEA9a1uf/31F1atWmVp9czMzITRaMQdd9yB6OhouLq6olevXli1apXlvMuXL8cnn3yCH374wXLcn3/+CQDIzs7GvHnz4OvrC61Wi5kzZyIzM7NVcROR82NiR0St9vzzz+OWW27B4cOH0bt3byxYsACLFi3C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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "082a4ad5-2917-497d-83b2-e34c16d1b89d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
