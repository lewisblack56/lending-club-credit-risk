# src/features.py
# Column categories from the notebook 03 audit. See 03_eda.ipynb for reasoning.

leakage_cols = [
    "total_pymnt", "total_pymnt_inv", "total_rec_prncp", "total_rec_int",
    "total_rec_late_fee", "last_pymnt_d", "last_pymnt_amnt", "next_pymnt_d",
    "out_prncp", "out_prncp_inv", "recoveries", "collection_recovery_fee",
    "last_fico_range_high", "last_fico_range_low", "last_credit_pull_d",
    "pymnt_plan", "hardship_flag", "hardship_type", "hardship_reason",
    "hardship_status", "deferral_term", "hardship_amount", "hardship_start_date",
    "hardship_end_date", "payment_plan_start_date", "hardship_length",
    "hardship_dpd", "hardship_loan_status",
    "orig_projected_additional_accrued_interest",
    "hardship_payoff_balance_amount", "hardship_last_payment_amount",
    "debt_settlement_flag",
]

lc_pricing_cols = ["grade", "sub_grade", "int_rate", "installment"]

id_text_cols = [
    "id", "url", "title", "emp_title", "policy_code",
    "funded_amnt", "funded_amnt_inv", "initial_list_status",
]

fair_lending_cols = ["addr_state", "zip_code"]

joint_cols = [
    "application_type", "annual_inc_joint", "dti_joint",
    "verification_status_joint", "revol_bal_joint",
    "sec_app_fico_range_low", "sec_app_fico_range_high",
    "sec_app_earliest_cr_line", "sec_app_inq_last_6mths", "sec_app_mort_acc",
    "sec_app_open_acc", "sec_app_revol_util", "sec_app_open_act_il",
    "sec_app_num_rev_accts", "sec_app_chargeoff_within_12_mths",
    "sec_app_collections_12_mths_ex_med",
]

late_added_cols = [
    "open_acc_6m", "open_act_il", "open_il_12m", "open_il_24m",
    "mths_since_rcnt_il", "total_bal_il", "il_util", "open_rv_12m",
    "open_rv_24m", "max_bal_bc", "all_util", "inq_fi", "total_cu_tl",
    "inq_last_12m",
]

meta_cols = ["loan_status", "issue_d", "term", "default", "sample",
             "quarter", "unresolved", "year"]

redundant_cols = ["fico_range_high"]   # always fico_range_low + 4

drop_list = (leakage_cols + lc_pricing_cols + id_text_cols + fair_lending_cols
             + joint_cols + late_added_cols + meta_cols + redundant_cols)

def get_candidate_features(df):
    return [c for c in df.columns if c not in drop_list]