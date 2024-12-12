<p>请求SPMM合约参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPMMINSTPARAM/">ReqQrySPMMInstParam</a>后，该方法被调用。</p>
<span class="anchor" id="e7753071-f810-4e1c-b153-2aa2b0f449f9"></span>
## 1.函数原型
<p>virtual void OnRspQrySPMMInstParam(CThostFtdcSPMMInstParamField *pSPMMInstParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="53095e1a-a6f8-4f2c-b4b2-b33860c42cda"></span>
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
<span class="anchor" id="99809ea5-bdf4-4955-9fbe-e5084307c2b6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ddfb8ec0-47e8-405f-bbe7-b6b9e54fe389"></span>
## 4.FAQ
<p>无</p>
