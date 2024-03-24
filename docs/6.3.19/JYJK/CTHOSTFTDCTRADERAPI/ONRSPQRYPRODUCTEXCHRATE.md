<p>请求查询产品报价汇率，当执行ReqQryProductExchRate后，该方法被调用。</p>
<span class="anchor" id="7797510a-7c4c-41cb-bab8-0b73344eb4a0"></span>
## 1.函数原型
<p>virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a1b9958f-23f6-425a-a5a0-bd3f92163bbd"></span>
## 2.参数
<p>pProductExchRate：产品报价汇率</p>
<pre><code>struct CThostFtdcProductExchRateField
{
    ///产品代码
    TThostFtdcInstrumentIDType ProductID;
    ///报价币种类型
    TThostFtdcCurrencyIDType QuoteCurrencyID;
    ///汇率
    TThostFtdcExchangeRateType ExchangeRate;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
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
<span class="anchor" id="9c166d01-ae05-47d5-a31a-03a625eab49a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="70441b41-f301-4839-b863-f6dadccb0c46"></span>
## 4.FAQ
<p>无</p>
