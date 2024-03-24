<p>询价通知，使用<a href="../../CTHOSTFTDCMDAPI/SUBSCRIBEFORQUOTERSP/">SubscribeForQuoteRsp</a>订阅该询价通知。私有流回报。</p>
<span class="anchor" id="a0307ec2-810c-40e7-a747-852331231620"></span>
## 1.函数原型
<p>virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {};</p>
<span class="anchor" id="722c55fb-ddc1-43cf-866b-09b228048cc3"></span>
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
<span class="anchor" id="9f75c2cc-40c6-4ccd-b7ff-64614b947f15"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ae5b7fd3-5eef-49bd-8753-4fccd5655a11"></span>
## 4.FAQ
<p>无</p>
