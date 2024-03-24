<p>请求查询投资者持仓响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPOSITION/">ReqQryInvestorPosition</a>后，该方法被调用。</p>
<p>CTP 系统将持仓明细记录按合约，持仓方向，开仓日期（仅针对上期所，区分昨仓、今仓）进行汇总。</p>
<blockquote>
<p>卖可平数量=多头仓-shortfrozen</p>
<p>买可平数量=空头仓-longfrozen</p>
</blockquote>
<span class="anchor" id="25bbbc65-9857-4d0a-8bb7-1fabd7760ec9"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="420fdfaf-3fe3-44bb-ad0f-ccef4832a03c"></span>
## 2.参数
<p>pInvestorPosition：投资者持仓</p>
<pre><code>struct CThostFtdcInvestorPositionField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///持仓多空方向
    TThostFtdcPosiDirectionType PosiDirection;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///持仓日期
    TThostFtdcPositionDateType  PositionDate;
    ///上日持仓
    TThostFtdcVolumeType    YdPosition;
    ///今日持仓
    TThostFtdcVolumeType    Position;
    ///多头冻结
    TThostFtdcVolumeType    LongFrozen;
    ///空头冻结
    TThostFtdcVolumeType    ShortFrozen;
    ///开仓冻结金额
    TThostFtdcMoneyType LongFrozenAmount;
    ///开仓冻结金额
    TThostFtdcMoneyType ShortFrozenAmount;
    ///开仓量
    TThostFtdcVolumeType    OpenVolume;
    ///平仓量
    TThostFtdcVolumeType    CloseVolume;
    ///开仓金额
    TThostFtdcMoneyType OpenAmount;
    ///平仓金额
    TThostFtdcMoneyType CloseAmount;
    ///持仓成本
    TThostFtdcMoneyType PositionCost;
    ///上次占用的保证金
    TThostFtdcMoneyType PreMargin;
    ///占用的保证金
    TThostFtdcMoneyType UseMargin;
    ///冻结的保证金
    TThostFtdcMoneyType FrozenMargin;
    ///冻结的资金
    TThostFtdcMoneyType FrozenCash;
    ///冻结的手续费
    TThostFtdcMoneyType FrozenCommission;
    ///资金差额
    TThostFtdcMoneyType CashIn;
    ///手续费
    TThostFtdcMoneyType Commission;
    ///平仓盈亏
    TThostFtdcMoneyType CloseProfit;
    ///持仓盈亏
    TThostFtdcMoneyType PositionProfit;
    ///上次结算价
    TThostFtdcPriceType PreSettlementPrice;
    ///本次结算价
    TThostFtdcPriceType SettlementPrice;
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///开仓成本
    TThostFtdcMoneyType OpenCost;
    ///交易所保证金
    TThostFtdcMoneyType ExchangeMargin;
    ///组合成交形成的持仓
    TThostFtdcVolumeType    CombPosition;
    ///组合多头冻结
    TThostFtdcVolumeType    CombLongFrozen;
    ///组合空头冻结
    TThostFtdcVolumeType    CombShortFrozen;
    ///逐日盯市平仓盈亏
    TThostFtdcMoneyType CloseProfitByDate;
    ///逐笔对冲平仓盈亏
    TThostFtdcMoneyType CloseProfitByTrade;
    ///今日持仓
    TThostFtdcVolumeType    TodayPosition;
    ///保证金率
    TThostFtdcRatioType MarginRateByMoney;
    ///保证金率(按手数)
    TThostFtdcRatioType MarginRateByVolume;
    ///执行冻结
    TThostFtdcVolumeType    StrikeFrozen;
    ///执行冻结金额
    TThostFtdcMoneyType StrikeFrozenAmount;
    ///放弃执行冻结
    TThostFtdcVolumeType    AbandonFrozen;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///执行冻结的昨仓
    TThostFtdcVolumeType    YdStrikeFrozen;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///持仓成本差值
    TThostFtdcMoneyType PositionCostOffset;
    ///tas持仓手数
    TThostFtdcVolumeType    TasPosition;
    ///tas持仓成本
    TThostFtdcMoneyType TasPositionCost;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
};
</code></pre>
<p>PositionProfit：期权没有持仓盈亏，为0</p>
<p>Position：表示当前持仓数量</p>
<p>TodayPosition：表示今新开仓</p>
<p>YdPosition：表示昨日收盘时持仓数量（≠ 当前的昨仓数量，静态，日间不随着开平仓而变化）</p>
<blockquote>
<p>当前的昨仓数量 = ∑Position -∑TodayPosition</p>
</blockquote>
<p>YdStrikeFrozen：该字段是给个股期权用的，期货期权里一直保持为0</p>
<p>PositionCost：持仓成本=上日持仓 * 昨结算价 * 合约乘数 + SUM（今日持仓 * 开仓价 * 合约乘数）</p>
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
<span class="anchor" id="adf94d81-202e-4f96-8c08-b40ecbc0842f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f2d443db-9e47-47d4-b4d7-f92a4886f015"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">投资者发现自己账号里面莫名其妙多了一条“PRT SR711&amp;SR711C6000"的持仓，是什么原因？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>这个合约是郑商所跨式，宽跨式期权组合合约。此合约不需要投资者使用特别的指令构建，只要客户持有可以构成备兑期权组合的持仓。在每日结算的时候，郑商所会将符合条件的期权和期货持仓自动确认为备兑期权套利持仓，包括备兑看涨期权套利和备兑看跌期权套利，并给予保证金优惠。</p>
<p>对于此期权合约，投资者需要分腿平仓，不需要管这个是否为备兑组合。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
