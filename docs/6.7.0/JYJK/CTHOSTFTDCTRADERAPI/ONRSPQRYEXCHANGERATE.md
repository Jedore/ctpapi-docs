<p>请求查询汇率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGERATE/">ReqQryExchangeRate</a>后，该方法被调用。</p>
<span class="anchor" id="2f54d7e6-eb01-4faf-8d76-c23aac816f27"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6b12e441-5034-4361-9073-9639dd785205"></span>
## 2.参数
<p>pExchangeRate：汇率</p>
<pre><code>struct CThostFtdcExchangeRateField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///源币种
    TThostFtdcCurrencyIDType FromCurrencyID;
    ///源币种单位数量
    TThostFtdcCurrencyUnitType FromCurrencyUnit;
    ///目标币种
    TThostFtdcCurrencyIDType ToCurrencyID;
    ///汇率
    TThostFtdcExchangeRateType ExchangeRate;
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
<span class="anchor" id="5a78dc06-600b-4d31-8c6b-ac0f00f9b258"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8af0c769-9b62-452e-86db-7c0002bcfd67"></span>
## 4.FAQ
<p>无</p>
