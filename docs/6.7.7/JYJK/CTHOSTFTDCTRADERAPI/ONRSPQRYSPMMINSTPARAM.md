<p>请求SPMM合约参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPMMINSTPARAM/">ReqQrySPMMInstParam</a>后，该方法被调用。</p>
<span class="anchor" id="accd4015-1410-4778-a49f-0a6d3df9087d"></span>
## 1.函数原型
<p>virtual void OnRspQrySPMMInstParam(CThostFtdcSPMMInstParamField *pSPMMInstParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1d7f3d08-f84f-4b38-b3d4-d03449fd2eec"></span>
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
<span class="anchor" id="6009db14-1edd-4d19-8a8f-6fe3eb1ac38a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="aa487f67-9891-42bc-a714-42fa3d9ee633"></span>
## 4.FAQ
<p>无</p>
