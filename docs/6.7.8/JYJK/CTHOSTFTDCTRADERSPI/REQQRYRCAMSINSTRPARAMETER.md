<p>请求RCAMS同合约风险对冲参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRCAMSINSTRPARAMETER/">OnRspQryRCAMSInstrParameter</a></p>
<span class="anchor" id="1798bc2f-e40d-4f25-9164-f6d3871f939e"></span>
## 1.函数原型
<p>virtual int ReqQryRCAMSInstrParameter(CThostFtdcQryRCAMSInstrParameterField *pQryRCAMSInstrParameter, int nRequestID) = 0;</p>
<span class="anchor" id="ae598b67-f613-49b7-b1fa-fd0034b0f19d"></span>
## 2.参数
<p>pQryRCAMSInstrParameter：RCAMS同合约风险对冲参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="0879403b-64a4-4148-8078-c9229ebd9b8d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="5b94fb5e-e350-48c5-ae0b-e4cd7a55def8"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="efd18e95-5f1d-4554-86e2-a8206a52fc51"></span>
## 5.FAQ
<p>无</p>
