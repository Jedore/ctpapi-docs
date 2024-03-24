<p>请求查询仓单折抵信息响应，当执行ReqQryEWarrantOffset后，该方法被调用。</p>
<span class="anchor" id="ae3ba7ea-f1a8-4957-896c-02cd57d97bc7"></span>
## 1.函数原型
<p>virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="f71b7b16-10de-4f09-955d-573367fe6f17"></span>
## 2.参数
<p>pEWarrantOffset：仓单折抵信息</p>
<pre><code>struct CThostFtdcEWarrantOffsetField
{
    ///交易日期
    TThostFtdcTradeDateType TradingDay;
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///数量
    TThostFtdcVolumeType Volume;
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
<span class="anchor" id="908c1110-b943-48e6-8141-e35921fb7a6b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6c451287-dcf0-4eb0-a796-169ccdc7d331"></span>
## 4.FAQ
<p>无</p>
