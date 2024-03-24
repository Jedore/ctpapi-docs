<p>请求查询资金账户响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRADINGACCOUNT/">ReqQryTradingAccount</a>后，该方法被调用。</p>
<span class="anchor" id="bf3e7ef4-aed7-446f-acec-e7a776ab9f56"></span>
## 1.函数原型
<p>virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1f666743-c1e6-4217-9bbd-ca0fbb792f6a"></span>
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
<p><span alt="" id="anchor-id-01"></span> </p>
<p>ReserveBalance：最低权益标准，对应柜台菜单“投资者最低权益设置”</p>
<p>Reserve：基础保证金，对应柜台菜单“投资者基础保证金设置”</p>
<p>PreCredit：上日资金冻结，为负值</p>
<p>Credit：当日资金冻结，为负值。交易系统初始化后会将PreCredit赋值给Credit，因此Credit包含了上日资金冻结和当日资金冻结。</p>
<p>PreBalance：昨权益</p>
<p>Balance：权益</p>
<p>FrozenCash：冻结权利金</p>
<p>CashIn：权利金</p>
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
<span class="anchor" id="efd4abc2-75c3-4f75-aa66-65f7e1b476a8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="64a3e6f5-0ecb-44bb-a428-5dd576237d71"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">期货品种的套保仓、投机仓、套利仓的单向大边是单独计算，还是一起计算的？对于能源中心INE目前的交易细则是不是也有单向大边的规则？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>单向大边目前只有上期所和中金所有此项业务。对于上期所，同品种的买卖双边分别计算，取买卖双边中保证金金额较大的一边单向实时收取。</p>
<p>对于中金所，套利、套保和投机的交易编码不同，计算的时候首先是区分交易编码的，每个交易编码下同品种的买卖双边再分别计算取大边。</p>
<p>对于能源中心，sc目前是单向大边的规则。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i"><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">关于冻结手续费计算的问题：比如我有大商所的持仓 i1709 10手昨仓，这个时候我平仓2手挂单了，请问此时的平仓手续费率是采用平昨手续费还是平今手续费，还是这两个费率取较大的？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>短线开平仓合约的平仓（不管平仓还是平今）在成交的时候是按平今手续费收取的，在冻结的时候是按平仓手续费收取。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
