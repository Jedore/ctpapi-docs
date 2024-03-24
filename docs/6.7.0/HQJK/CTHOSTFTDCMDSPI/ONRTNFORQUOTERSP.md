<p>询价通知，使用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>订阅该询价通知。私有流回报。</p>
<span class="anchor" id="42c1000d-0417-4a3e-bf15-b45e917d2f44"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="e4a0e932-1be3-4208-8857-09f42cc85b73"></span>
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
<span class="anchor" id="3651a50f-f902-4290-9273-3dfa6451707d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2e4ad48e-99b8-422b-8e6c-b5296e5f9b88"></span>
## 4.FAQ
<p>无</p>
