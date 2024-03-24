<p>请求查询投资者持仓明细响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPOSITIONCOMBINEDETAIL/">ReqQryInvestorPositionCombineDetail</a>后，该方法被调用。</p>
<span class="anchor" id="34a72dfb-f4d2-4107-90cf-64a94d27acd2"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8de96728-6908-46a2-a4d5-9670c4864433"></span>
## 2.参数
<p>pInvestorPositionCombineDetail：投资者组合持仓明细</p>
<pre><code>struct CThostFtdcInvestorPositionCombineDetailField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///开仓日期
    TThostFtdcDateType  OpenDate;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///结算编号
    TThostFtdcSettlementIDType  SettlementID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///组合编号
    TThostFtdcTradeIDType   ComTradeID;
    ///撮合编号
    TThostFtdcTradeIDType   TradeID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///买卖
    TThostFtdcDirectionType Direction;
    ///持仓量
    TThostFtdcVolumeType    TotalAmt;
    ///投资者保证金
    TThostFtdcMoneyType Margin;
    ///交易所保证金
    TThostFtdcMoneyType ExchMargin;
    ///保证金率
    TThostFtdcRatioType MarginRateByMoney;
    ///保证金率(按手数)
    TThostFtdcRatioType MarginRateByVolume;
    ///单腿编号
    TThostFtdcLegIDType LegID;
    ///单腿乘数
    TThostFtdcLegMultipleType   LegMultiple;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve2;
    ///成交组号
    TThostFtdcTradeGroupIDType  TradeGroupID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///组合持仓合约编码
    TThostFtdcInstrumentIDType  CombInstrumentID;
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
<span class="anchor" id="41f1c7b1-e870-4fd8-8df7-776da635fee1"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8ea842ff-8db0-4707-8d04-8fbde9a967ea"></span>
## 4.FAQ
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">组合持仓明细应该如何去判断谁和谁是一对？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>用ComTradeID判断。注意以下几点：</p>
<p>1) ComTradeID是CTP定义的。盘中新开仓的时候ComTradeID比如是115，在盘后结算完成后为了防止重复会重新打上编号，编号里带上交易日，如20170720000003；</p>
<p>2) ComTradeID并不一定是成对出现。比如下单五手组合合约：左腿全部成交，右腿是分笔成交的1，1，3的方式成交的。所以总的收到的成交回报就会有4条。这四条的ComTradeID，在盘中是一致的。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
