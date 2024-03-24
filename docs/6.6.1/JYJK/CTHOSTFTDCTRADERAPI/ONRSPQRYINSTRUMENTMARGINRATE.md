<p>请求查询合约保证金率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENTMARGINRATE/">ReqQryInstrumentMarginRate</a>后，该方法被调用。</p>
<span class="anchor" id="ab0cb5c2-8f34-43b6-bd2f-2175785276fb"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a3f15ff5-65cd-4a4c-b11e-b34f396386ad"></span>
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
<span class="anchor" id="72dc0ba9-9ed3-465b-87e4-d572455ebe44"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9df83cd2-6375-42ac-b7e0-7a4f785551f4"></span>
## 4.FAQ
<p>无</p>
