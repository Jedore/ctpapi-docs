<p>请求查询产品报价汇率，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCTEXCHRATE/">ReqQryProductExchRate</a>后，该方法被调用。</p>
<span class="anchor" id="91a69b6c-aab7-438c-9101-1871ddd37fea"></span>
## 1.函数原型
<p>virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="ef8c2f48-9764-44b0-b558-dfd3212642af"></span>
## 2.参数
<p>pProductExchRate：产品报价汇率</p>
<pre><code>struct CThostFtdcProductExchRateField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///报价币种类型
    TThostFtdcCurrencyIDType    QuoteCurrencyID;
    ///汇率
    TThostFtdcExchangeRateType  ExchangeRate;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///产品代码
    TThostFtdcInstrumentIDType  ProductID;
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
<span class="anchor" id="327b55bf-86bd-4361-970d-211167c33a9b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="4f9a4c26-9f66-4af8-8379-4f536b18a44b"></span>
## 4.FAQ
<p>无</p>
