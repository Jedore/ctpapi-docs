<p>请求查询资金账户响应</p>
<span class="anchor" id="55268c40-9ccd-41f4-9a72-143ac00232e3"></span>
## 1.函数原型
<p>virtual void OnRspQrySecAgentTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="bbe5fb35-061e-4376-a2f7-93ef64942f55"></span>
## 2.参数
<p>pTradingAccount：资金账户</p>
<pre><code>struct CThostFtdcTradingAccountField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///上次质押金额
    TThostFtdcMoneyType PreMortgage;
    ///上次信用额度
    TThostFtdcMoneyType PreCredit;
    ///上次存款额
    TThostFtdcMoneyType PreDeposit;
    ///上次结算准备金
    TThostFtdcMoneyType PreBalance;
    ///上次占用的保证金
    TThostFtdcMoneyType PreMargin;
    ///利息基数
    TThostFtdcMoneyType InterestBase;
    ///利息收入
    TThostFtdcMoneyType Interest;
    ///入金金额
    TThostFtdcMoneyType Deposit;
    ///出金金额
    TThostFtdcMoneyType Withdraw;
    ///冻结的保证金
    TThostFtdcMoneyType FrozenMargin;
    ///冻结的资金
    TThostFtdcMoneyType FrozenCash;
    ///冻结的手续费
    TThostFtdcMoneyType FrozenCommission;
    ///当前保证金总额
    TThostFtdcMoneyType CurrMargin;
    ///资金差额
    TThostFtdcMoneyType CashIn;
    ///手续费
    TThostFtdcMoneyType Commission;
    ///平仓盈亏
    TThostFtdcMoneyType CloseProfit;
    ///持仓盈亏
    TThostFtdcMoneyType PositionProfit;
    ///期货结算准备金
    TThostFtdcMoneyType Balance;
    ///可用资金
    TThostFtdcMoneyType Available;
    ///可取资金
    TThostFtdcMoneyType WithdrawQuota;
    ///基本准备金
    TThostFtdcMoneyType Reserve;
    ///交易日
    TThostFtdcDateType TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType SettlementID;
    ///信用额度
    TThostFtdcMoneyType Credit;
    ///质押金额
    TThostFtdcMoneyType Mortgage;
    ///交易所保证金
    TThostFtdcMoneyType ExchangeMargin;
    ///投资者交割保证金
    TThostFtdcMoneyType DeliveryMargin;
    ///交易所交割保证金
    TThostFtdcMoneyType ExchangeDeliveryMargin;
    ///保底期货结算准备金
    TThostFtdcMoneyType ReserveBalance;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///上次货币质入金额
    TThostFtdcMoneyType PreFundMortgageIn;
    ///上次货币质出金额
    TThostFtdcMoneyType PreFundMortgageOut;
    ///货币质入金额
    TThostFtdcMoneyType FundMortgageIn;
    ///货币质出金额
    TThostFtdcMoneyType FundMortgageOut;
    ///货币质押余额
    TThostFtdcMoneyType FundMortgageAvailable;
    ///可质押货币金额--已废弃
    TThostFtdcMoneyType MortgageableFund;
    ///特殊产品占用保证金--已废弃
    TThostFtdcMoneyType SpecProductMargin;
    ///特殊产品冻结保证金--已废弃 
    TThostFtdcMoneyType SpecProductFrozenMargin;
    ///特殊产品手续费--已废弃
    TThostFtdcMoneyType SpecProductCommission;
    ///特殊产品冻结手续费--已废弃
    TThostFtdcMoneyType SpecProductFrozenCommission;
    ///特殊产品持仓盈亏--已废弃
    TThostFtdcMoneyType SpecProductPositionProfit;
    ///特殊产品平仓盈亏--已废弃
    TThostFtdcMoneyType SpecProductCloseProfit;
    ///根据持仓盈亏算法计算的特殊产品持仓盈亏--已废弃
    TThostFtdcMoneyType SpecProductPositionProfitByAlg;
    ///特殊产品交易所保证金--已废弃
    TThostFtdcMoneyType SpecProductExchangeMargin;
    ///业务类型
    TThostFtdcBizTypeType BizType;
    ///延时换汇冻结金额
    TThostFtdcMoneyType FrozenSwap;
    ///剩余换汇额度
    TThostFtdcMoneyType RemainSwap;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="535779cb-e5ed-4495-a9ad-8fe44db85ac6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8e1e044b-a351-4614-bae9-2915323aa24c"></span>
## 4.FAQ
<p>无</p>
