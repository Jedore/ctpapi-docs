<p>请求SPMM产品参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPMMPRODUCTPARAM/">ReqQrySPMMProductParam</a>后，该方法被调用。</p>
<span class="anchor" id="1585ede2-f978-477e-b8c0-81d4ea1beab6"></span>
## 1.函数原型
<p>virtual void OnRspQrySPMMProductParam(CThostFtdcSPMMProductParamField *pSPMMProductParam, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="497d0630-a499-4dfc-b8c1-a8e6928fa892"></span>
## 2.参数
<p>pSPMMProductParam：SPMM产品参数</p>
<pre><code>struct CThostFtdcSPMMProductParamField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///产品代码
    TThostFtdcSPMMProductIDType ProductID;
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
<span class="anchor" id="5306792b-d38d-46b2-813d-832936553d32"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="0ce1d535-4bc3-429f-b593-5da471c7758b"></span>
## 4.FAQ
<p>无</p>
