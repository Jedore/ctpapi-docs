<p>请求查询报单手续费响应，当执行ReqQryInstrumentOrderCommRate后，该方法被调用。</p>
<span class="anchor" id="c3c3b6eb-a187-4b18-b7ac-5883f0087878"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e4344489-e766-4fa7-863b-75606a630b2f"></span>
## 2.参数
<p>pInstrumentOrderCommRate：当前报单手续费的详细内容</p>
<pre><code>struct CThostFtdcInstrumentOrderCommRateField
{
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///报单手续费
    TThostFtdcRatioType OrderCommByVolume;
    ///撤单手续费
    TThostFtdcRatioType OrderActionCommByVolume;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="78cab57c-9721-4613-b3eb-441f031da2bd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ef4e3328-a7a8-40d8-b05f-9c2866adcf78"></span>
## 4.FAQ
<p>无</p>
