<p>请求查询产品报价汇率，当执行ReqQryProductExchRate后，该方法被调用。</p>
<span class="anchor" id="ff2a5567-eecb-49e5-be58-77792e5ccb27"></span>
## 1.函数原型
<p>virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="409b46f5-8eb7-45e2-b259-f758bdff009b"></span>
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
<span class="anchor" id="64060e8b-87dc-4e5d-b95f-3fb7ef6dc437"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0fada085-e567-4f4f-9812-e8940a24feaf"></span>
## 4.FAQ
<p>无</p>
