<p>请求查询汇率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGERATE/">ReqQryExchangeRate</a>后，该方法被调用。</p>
<span class="anchor" id="0d1f2538-ee7a-4133-a33e-9030f5513671"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="ca8c44b9-338a-4af2-b1e5-eaf6e1efbef4"></span>
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
<span class="anchor" id="4ce7ee08-3195-4252-829d-5b17be7161fd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c48c2830-f785-43c1-84eb-92f1120576f5"></span>
## 4.FAQ
<p>无</p>
