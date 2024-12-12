<p>请求查询产品报价汇率，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCTEXCHRATE/">ReqQryProductExchRate</a>后，该方法被调用。</p>
<span class="anchor" id="49baf2c0-4b1f-41e0-a5ac-19cefecf9b52"></span>
## 1.函数原型
<p>virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b5fc8f42-fe5e-4aa4-948c-e377b3e08008"></span>
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
<span class="anchor" id="774acbe3-3e6a-4a33-b7f4-9a45e6d8cfca"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6ceeed97-112b-477e-8cc6-3a1ff5f6af6a"></span>
## 4.FAQ
<p>无</p>
