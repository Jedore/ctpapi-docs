<p>询价通知，使用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>订阅该询价通知。私有流回报。</p>
<span class="anchor" id="14f28c78-7785-42a7-b61d-5a06015d5a29"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="de8d3254-282b-4205-a123-cd28919faee7"></span>
## 2.参数
<p>pForQuoteRsp：发给做市商的询价请求</p>
<pre><code>struct CThostFtdcForQuoteRspField
{
    ///交易日
    TThostFtdcDateType TradingDay;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///询价编号
    TThostFtdcOrderSysIDType ForQuoteSysID;
    ///询价时间
    TThostFtdcTimeType ForQuoteTime;
    ///业务日期
    TThostFtdcDateType ActionDay;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
};
</code></pre>
<p>ForQuoteSysID：交易所给的一个询价编号，以此定位一笔询价。</p>
<span class="anchor" id="1ed4db45-c83f-4f4d-9bf8-3d326b8226cf"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2e4035e2-cf5f-4c25-8305-2397bc44f4f0"></span>
## 4.FAQ
<p>无</p>
