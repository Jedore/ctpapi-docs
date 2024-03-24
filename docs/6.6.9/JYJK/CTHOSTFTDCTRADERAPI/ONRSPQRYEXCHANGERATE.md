<p>请求查询汇率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGERATE/">ReqQryExchangeRate</a>后，该方法被调用。</p>
<span class="anchor" id="14b883d0-0f8e-4425-a8f8-b86171945320"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a03d335c-65b9-4219-88e6-e4f0ba088f71"></span>
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
<span class="anchor" id="50e4227a-94d5-4ad9-b040-f82771d8f425"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="beb01996-02fd-4f36-97e2-9a7b4f59f851"></span>
## 4.FAQ
<p>无</p>
