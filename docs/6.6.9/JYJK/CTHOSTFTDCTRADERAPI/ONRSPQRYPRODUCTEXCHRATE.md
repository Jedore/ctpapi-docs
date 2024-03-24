<p>请求查询产品报价汇率，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYPRODUCTEXCHRATE/">ReqQryProductExchRate</a>后，该方法被调用。</p>
<span class="anchor" id="937a4f7c-28a9-420b-ab56-2436897717a2"></span>
## 1.函数原型
<p>virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8c2d8690-d8f7-4b76-b3b8-1b82fae2c635"></span>
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
<span class="anchor" id="774aa667-03dc-4924-8ba0-756232d5b0a6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3374dae7-47e9-44fc-bbc1-3d23af4d28c8"></span>
## 4.FAQ
<p>无</p>
