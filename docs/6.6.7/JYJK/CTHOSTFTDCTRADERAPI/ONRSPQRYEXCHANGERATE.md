<p>请求查询汇率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGERATE/">ReqQryExchangeRate</a>后，该方法被调用。</p>
<span class="anchor" id="26dd0148-9d87-44e6-89b7-e615a7411746"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="61d994f9-ae99-441c-bfaf-8fdae29a1ea5"></span>
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
<span class="anchor" id="48505a20-5e2c-4703-8e88-90b24f5c79a8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ca7ddac7-0c88-486a-b8c2-9d992be91b1c"></span>
## 4.FAQ
<p>无</p>
