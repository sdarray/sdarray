import numpy as np
import pandas as pd
import sdarray as sd


# test data for evaluation
shape = 3600, 100
date = "2020-01-01"
label = ["ON,SCI", "OFF,CAL"]

t = pd.date_range(date, periods=shape[0], freq="1s").to_numpy()
ch = np.arange(shape[1])
label = "t", np.random.choice(label, shape[0])

da = sd.array(np.random.randn(*shape), t=t, ch=ch, coords={"label": label})


# test functions
def test_eq(n_ch=10):
    ch_sel = np.random.choice(ch, n_ch, False)
    da_ans = da.loc[:, ch_sel]
    da_test = da.sd.where("ch") == ch_sel
    assert (da_test == da_ans).all()


def test_neq(n_ch=10):
    ch_sel = np.random.choice(ch, n_ch, False)
    da_ans = da.loc[:, np.setdiff1d(ch, ch_sel)]
    da_test = da.sd.where("ch") != ch_sel
    assert (da_test == da_ans).all()


def test_gt(ch_max=50):
    da_ans = da.loc[:, ch[ch > ch_max]]
    da_test = da.sd.where("ch") > ch_max
    assert (da_test == da_ans).all()


def test_gt_or_eq(ch_max=50):
    da_ans = da.loc[:, ch[ch >= ch_max]]
    da_test = da.sd.where("ch") >= ch_max
    assert (da_test == da_ans).all()


def test_lt(ch_max=50):
    da_ans = da.loc[:, ch[ch < ch_max]]
    da_test = da.sd.where("ch") < ch_max
    assert (da_test == da_ans).all()


def test_lt_or_eq(ch_max=50):
    da_ans = da.loc[:, ch[ch <= ch_max]]
    da_test = da.sd.where("ch") <= ch_max
    assert (da_test == da_ans).all()


def test_between_1d(ch_min=10, ch_max=50):
    da_ans = da.loc[:, ch[(ch >= ch_min) & (ch <= ch_max)]]
    da_test = da.sd.where("ch") @ (ch_min, ch_max)
    assert (da_test == da_ans).all()


def test_between_2d(t_min="00:30:00", t_max="00:45:00", ch_min=10, ch_max=50):
    t_min = np.datetime64(f"{date}T{t_min}")
    t_max = np.datetime64(f"{date}T{t_max}")
    t_bool = (t >= t_min) & (t <= t_max)
    ch_bool = (ch >= ch_min) & (ch <= ch_max)

    da_ans = da.loc[t[t_bool], ch[ch_bool]]
    da_test = da.sd.where("t", "ch") @ ((t_min, t_max), (ch_min, ch_max))
    assert (da_test == da_ans).all()


def test_contains(label="ON", label_ans="ON,SCI"):
    da_ans = da[da.label == label_ans]
    da_test = da.sd.where("label") ** label
    assert (da_test == da_ans).all()
