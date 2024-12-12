<p>请求投资者投资者新组保设置查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFSETTING/">ReqQryInvestorPortfSetting</a>后，该方法被调用。</p>
<span class="anchor" id="d43bc964-f14a-4354-a9cd-153629dce61e"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorInfoCommRec(CThostFtdcInvestorInfoCommRecField *pInvestorInfoCommRec, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d91359af-37dd-406f-b082-d627ed2612b5"></span>
## 2.参数
<p>pInvestorInfoCommRec：投资者申报费阶梯收取记录</p>
<pre><code>struct CThostFtdcInvestorInfoCommRecField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///商品代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///报单总笔数
    TThostFtdcVolumeType    OrderCount;
    ///撤单总笔数
    TThostFtdcVolumeType    OrderActionCount;
    ///询价总次数
    TThostFtdcVolumeType    ForQuoteCnt;
    ///申报费
    TThostFtdcMoneyType InfoComm;
    ///是否期权系列
    TThostFtdcBoolType  IsOptSeries;
    ///品种代码
    TThostFtdcProductIDType ProductID;
    ///信息量总量
    TThostFtdcVolumeType    InfoCnt;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
};
</code></pre>
<span class="anchor" id="8939bb53-7a75-4cd9-b552-3c1920b15bef"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="26a376ce-8322-4924-b634-dd2d4fdfe03e"></span>
## 4.FAQ
<p>无</p>
