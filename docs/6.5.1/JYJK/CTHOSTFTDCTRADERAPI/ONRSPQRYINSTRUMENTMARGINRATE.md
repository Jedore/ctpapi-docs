<p>请求查询合约保证金率响应，当执行ReqQryInstrumentMarginRate后，该方法被调用。</p>
<span class="anchor" id="e1e39d8d-0c71-41af-a0c0-477d637d8f63"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="7e6efbe1-2505-49f8-bcdf-3c12719a649a"></span>
## 2.参数
<p>///pInstrumentMarginRate：合约保证金率</p>
<pre><code>struct CThostFtdcInstrumentMarginRateField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///多头保证金率
    TThostFtdcRatioType LongMarginRatioByMoney;
    ///多头保证金费
    TThostFtdcMoneyType LongMarginRatioByVolume;
    ///空头保证金率
    TThostFtdcRatioType ShortMarginRatioByMoney;
    ///空头保证金费
    TThostFtdcMoneyType ShortMarginRatioByVolume;
    ///是否相对交易所收取
    TThostFtdcBoolType  IsRelative;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<span class="anchor" id="228c0097-37e7-4ee0-b976-36830cb32d6f"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="34047e9a-11d1-4546-a62f-8d53765f2f10"></span>
## 4.FAQ
<p>无</p>
