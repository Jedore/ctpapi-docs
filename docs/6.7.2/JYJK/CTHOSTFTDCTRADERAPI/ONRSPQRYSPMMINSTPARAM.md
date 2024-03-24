<p>请求SPMM合约参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPMMINSTPARAM/">ReqQrySPMMInstParam</a>后，该方法被调用。</p>
<span class="anchor" id="0929827a-5ee7-4712-9083-a56dec335e0c"></span>
## 1.函数原型
<p>virtual void OnRspQrySPMMInstParam(CThostFtdcSPMMInstParamField *pSPMMInstParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6ae47b33-95de-4dbe-a497-74f1576af039"></span>
## 2.参数
<p>pSPMMInstParam：SPMM合约参数</p>
<pre><code>struct CThostFtdcSPMMInstParamField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///SPMM合约保证金算法
    TThostFtdcInstMarginCalIDType   InstMarginCalID;
    ///商品组代码
    TThostFtdcSPMMProductIDType CommodityID;
    ///商品群代码
    TThostFtdcSPMMProductIDType CommodityGroupID;
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
<span class="anchor" id="126967c0-50f5-48aa-a9cf-6f3bfc9ce6a7"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="6a1f2a75-2138-44c0-8e76-f602a0deecbc"></span>
## 4.FAQ
<p>无</p>
